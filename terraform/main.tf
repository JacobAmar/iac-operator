resource "random_pet" "name" {
  length    = 2
  keepers = {
    id = value
  }
}
