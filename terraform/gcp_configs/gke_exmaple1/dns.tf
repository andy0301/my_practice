# Create DNS

# create dns zone
resource "google_dns_managed_zone" "gke_example1_dns_zone" {
  name        = "gke-example1-dns"
  dns_name    = "web-example.com."
  description = "Web example DNS zone"
  labels = {
    sample = "web-example1"
  }
}

resource "random_id" "rnd" {
  byte_length = 4
}

# create dns policy
#resource "google_dns_policy" "gke_example1_dns_policy" {

#}

# create record set
resource "google_dns_record_set" "frontend" {
  name = "frontend.google_dns_managed_zone.gke_example1_dns_zone.dns_name"
  type = "A"
  ttl  = 300

  managed_zone = google_dns_managed_zone.gke_example1_dns_zone.dns_name

  rrdatas = ["34.107.231.173"]
}