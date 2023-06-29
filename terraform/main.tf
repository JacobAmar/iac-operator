resource "random_pet" "name" {
  length    = 2
}

locals {
    name = "${random_pet.name.id}-${var.region}"
}

variable "region" {
  type        = string
}

output "final" {
  value       = local.name
}

