# Overview
This is a simple demo to compare Pulumi and Terraform. We will create and S3 bucket using both technologies.

## Terraform
Run the following commands:

```bash
export AWS_ACCESS_KEY_ID=your-access-key-id
export AWS_SECRET_ACCESS_KEY=your-secret-access-key
terraform init
terraform plan
terraform apply
```


## Pulumi
Run the following commands:

```bash
export AWS_ACCESS_KEY_ID=your-access-key-id
export AWS_SECRET_ACCESS_KEY=your-secret-access-key
pulumi new
pulumi preview
pulumi up
```