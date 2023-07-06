from git import Repo, Head, Remote, repo
import os


def git_handler(repository,path,branch=None):
        if os.path.exists(path) == False:
           print(f"cloning the repository: {repository}")
           Repo.clone_from(repository,to_path=path,branch=branch)
        else:
                repo = Repo(path)
                remote = repo.remote(name='origin')
                if branch == None:
                    print(f"pulling changes for repo {repository}")
                    remote.pull()
                else:
                      # checking out to the spesific branch address any changes on the branch name
                      Head.checkout(path)
                      print(f"pulling changes for repo {repository}")
                      remote.pull()