output "public_ip" {
  value       = aws_instance.andy_instance_001.public_ip
  description = "The public ip address of the web server."
  # sensitive   = true
}
