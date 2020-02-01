output "alb_dns_name" {
  value       = aws_lb.andy_lb_example.dns_name
  description = "This is domain of loadbalancer."
}
