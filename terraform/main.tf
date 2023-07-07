resource "random_pet" "name" {
  length    = 3
}

locals {
    name = "${random_pet.name.id}-${var.region}"
    cidr_blocks = { for key,val in var.vpc_cidrs: key => val }
}

variable "region" {
  type        = string
}

variable "vpc_cidrs" {}

output "final" {
  value       = local.name
}

output "cidr_blocks" {
  value       = local.cidr_blocks
}
