# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
        name="Atanu Biswas",
        title="Hybrid Cloud Engineer",
        contact={
            'email': '09atanu@gmail.com',
            'phone': '+8801920287188',
            'location': 'Dhaka, Bangladesh',
            'linkedin': 'https://linkedin.com/in/atanu09'
        },
        skills={
            'System Management': ['Windows & Linux Server Administration', 'Proxy, DNS, DHCP', 'Active Directory'],
            'DevOps': ['Docker', 'Kubernetes', 'Jenkins', 'GitLab CI/CD'],
            'Cloud & Virtualization': ['Azure', 'VMware vSphere', 'AWS', 'GCP'],
            'Security': ['EDR/XDR', 'MS Zero Trust', 'VA-PT', 'Security Hardening'],
            'Networking': ['CISCO', 'Meraki SD-WAN', 'Mikrotik', 'VPN']
        },
        experience=[
            {
                'title': 'Hybrid Cloud Engineer',
                'company': 'Transcom Limited',
                'duration': '2022 - Present',
                'achievements': [
                    'Achieved 99.9% uptime through infrastructure optimization',
                    'Reduced vulnerabilities by 40% through security implementations',
                    'Managed 100+ VMs and databases with Acronis Backup'
                ]
            },
            # Add other experiences similarly
        ],
        certifications=[
            'Microsoft Certified: Azure Administrator Associate',
            'Network Defense Essentials (NDE)',
            'VMware vSphere Certification'
        ],
        education=[
            {
                'degree': 'B.Sc. in Electronics & Communication',
                'institution': 'Khulna University',
                'year': '2013'
            }
        ]
    )

if __name__ == '__main__':