class SecurityIncident:
    def __init__(self, incident_type, description):
        self.incident_type = incident_type
        self.description = description

    def __str__(self):
        return f"Type: {self.incident_type}\nDescription: {self.description}\n"

class IncidentReporter:
    def __init__(self):
        self.incidents = []

    def report_incident(self, incident_type, description):
        incident = SecurityIncident(incident_type, description)
        self.incidents.append(incident)
        print("Incident reported successfully")

    def show_reports(self):
        if not self.incidents:
            print("No incidents reported")
        else:
            for idx, incident in enumerate(self.incidents, 1):
                print(f"Incident {idx}:\n{incident}")

def main():
    reporter = IncidentReporter()
    while True:
        print("\nSecurity Incident Reporting Tool")
        print("1. Report an incident")
        print("2. Show all incidents")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            incident_type = input("Enter the type of incident: ")
            description = input("Enter a description of the incident: ")
            reporter.report_incident(incident_type, description)
        elif choice == "2":
            reporter.show_reports()
        elif choice == "3":
            print("Exiting the tool")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
