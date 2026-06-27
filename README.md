# Shared Finance Platform

A cloud-native financial analytics platform designed to help couples manage shared expenses, savings goals, and financial planning.

## Goals

- Integrate with Google Sheets as source of truth
- Provide financial insights and analytics
- Demonstrate modern backend engineering practices
- Showcase DevOps and SRE skills

## Technology Stack

- Python
- Flask
- Docker
- PostgreSQL
- Google Sheets API
- Azure Container Apps
- GitHub Actions
- Terraform

## Architecture

The project follows a Clean Architecture approach:

- API Layer
- Application Layer
- Domain Layer
- Infrastructure Layer

## Configuration

1. Copy `.env.example` to `.env`
2. Configure your Google Spreadsheet ID
3. Run `make run`