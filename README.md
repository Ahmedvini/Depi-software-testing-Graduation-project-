# 🎓 DEPI Graduation Project - Performance Testing Framework

## Software Testing Track 

### 👥 Team Members
- Ahmed ElSheikh
- Youssef Farid
- Ahmed Tahoun
- Abdullah Mohamed Abdullah

## 📋 Project Overview
This project is a comprehensive performance testing framework developed as part of the DEPI (Digital Egypt Builders Initiative) Software Testing Track graduation project. The framework utilizes Locust for load testing and integrates with CI/CD pipelines through GitHub Actions.

## 🎯 Project Objectives
- Implement automated performance testing
- Integrate with CI/CD pipelines
- Provide real-time performance metrics
- Generate comprehensive test reports
- Set and monitor performance thresholds
- Enable cloud-based distributed load testing

## 🛠 Technical Stack
- **Load Testing Tool**: Locust
- **Programming Language**: Python
- **CI/CD**: GitHub Actions
- **Version Control**: Git
- **Reporting**: HTML & CSV Reports
- **APIs Tested**: Restful Booker API

## 📊 Features
1. **Automated Load Testing**
   - Configurable number of users
   - Adjustable spawn rates
   - Custom test scenarios

2. **Performance Metrics**
   - Average Response Time
   - 95th Percentile Response Time
   - Failure Ratio
   - Requests per Second
   - Custom Thresholds

3. **CI/CD Integration**
   - Automated test execution
   - Performance regression detection
   - Threshold-based alerts
   - Artifact storage

4. **Reporting**
   - Real-time metrics dashboard
   - HTML test reports
   - CSV data export
   - Failure analysis

## 🚀 Getting Started

### Prerequisites
```bash
python 3.x
pip
git
```

### Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd depi
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Tests Locally
1. Basic test execution:
```bash
locust -f locustfile.py
```

2. Headless mode with parameters:
```bash
locust -f locustfile.py --headless -u 100 -r 5 -t 5m
```

3. View results at: http://localhost:8089

## 📈 Performance Thresholds
Current performance thresholds are set to:
- Average Response Time: 1000ms (1 second)
- 95th Percentile Response Time: 3000ms (3 seconds)
- Failure Ratio: 1% (0.01)

## 🔄 CI/CD Pipeline
The project includes a GitHub Actions workflow that:
1. Runs automated load tests
2. Validates performance thresholds
3. Generates and stores test reports
4. Creates issues for test failures

## 📊 Test Reports
Reports are generated in multiple formats:
- HTML reports with graphs and charts
- CSV files with raw data
- GitHub Actions artifacts
- Real-time metrics during test execution

## 🌐 Cloud Integration
Support for distributed load testing using:
- Azure Load Testing
- AWS Distributed Load Testing
- Google Cloud Load Testing

## 📝 Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## 📄 License
This project is part of the DEPI graduation requirements and is subject to DEPI's terms and conditions.

## 🙏 Acknowledgments
- DEPI Program Mentors and Instructors
- Software Testing Track Supervisors
- Restful Booker API Team

---
*This project was developed as part of the Digital Egypt Builders Initiative (DEPI) Software Testing Track graduation requirements.* 
