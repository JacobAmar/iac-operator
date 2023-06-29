from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Controller(BaseHTTPRequestHandler):
  def sync(self, parent, children):
    # Compute status based on observed state.
    desired_status = {
      "pods": len(children["Pod.v1"])
    }
    name = parent["metadata"]["name"]
    repository = parent["spec"]["repository"]
    path = parent["spec"]["path"]
    # Generate the desired child object(s).
    desired_manifests = [
        {
          "apiVersion": "v1",
          "kind": "Pod",
          "metadata": {
            "labels": {
              "run": f"{name}-terraform-plan"
            },
            "name": f"{name}-terraform-plan"
          },
          "spec": {
            "containers": [
              {
                "image": "hashicorp/terraform:1.5",
                "name": f"{name}-terraform-plan",
                "command": [
                  "/bin/sh",
                  "-c",
                  f"cd /data\nls -la\ncd {path}\n cat main.tf"
                ],
                "volumeMounts": [
                  {
                    "mountPath": "/data",
                    "name": "terraform-dir"
                  }
                ]
              }
            ],
            "initContainers": [
              {
                "name": "git-cloner",
                "image": "alpine/git",
                "args": [
                  "clone",
                  "--single-branch",
                  "--",
                  repository,
                  "/data"
                ],
                "volumeMounts": [
                  {
                    "mountPath": "/data",
                    "name": "terraform-dir"
                  }
                ]
              }
            ],
            "volumes": [
              {
                "name": "terraform-dir",
                "emptyDir": {}
              }
            ]
          }
        }
    ]

    return {"status": desired_status, "children": desired_manifests}

  def do_POST(self):
    # Serve the sync() function as a JSON webhook.
    observed = json.loads(self.rfile.read(int(self.headers.get("content-length"))))
    desired = self.sync(observed["parent"], observed["children"])

    self.send_response(200)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(desired).encode())

HTTPServer(("", 80), Controller).serve_forever()
