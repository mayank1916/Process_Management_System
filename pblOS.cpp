#include <iostream>
using namespace std;

#define MAX 10

// Process structure
struct Process {
    int pid;
    string state;
};

Process p[MAX];
int count = 0;

// Create Process
void createProcess() {
    if (count >= MAX) {
        cout << "Process limit reached!\n";
        return;
    }

    p[count].pid = count + 1;
    p[count].state = "Ready";

    cout << "Process Created! PID = " << p[count].pid << endl;
    count++;
}

// Display Processes
void displayProcess() {
    if (count == 0) {
        cout << "No processes available!\n";
        return;
    }

    cout << "\nPID\tState\n";
    for (int i = 0; i < count; i++) {
        cout << p[i].pid << "\t" << p[i].state << endl;
    }
}

// Change Process State
void changeState() {
    int id;
    cout << "Enter PID: ";
    cin >> id;

    for (int i = 0; i < count; i++) {
        if (p[i].pid == id) {
            cout << "Enter new state (Ready/Running/Waiting): ";
            cin >> p[i].state;
            cout << "State Updated!\n";
            return;
        }
    }

    cout << "Process not found!\n";
}

// Delete Process
void deleteProcess() {
    int id;
    cout << "Enter PID to delete: ";
    cin >> id;

    for (int i = 0; i < count; i++) {
        if (p[i].pid == id) {
            // for (int j = i; j < count - 1; j++) {
            //     p[j] = p[j + 1];
            // }
            count--;
            cout << "Process Deleted!\n";
            return;
        }
    }

    cout << "Process not found!\n";
}

// Main Menu
int main() {
    int choice;

    while (true) {
        cout << "\n--- Process Management System ---\n";
        cout << "1. Create Process\n";
        cout << "2. Display Processes\n";
        cout << "3. Change Process State\n";
        cout << "4. Delete Process\n";
        cout << "5. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        switch (choice) {
            case 1: createProcess(); break;
            case 2: displayProcess(); break;
            case 3: changeState(); break;
            case 4: deleteProcess(); break;
            case 5: return 0;
            default: cout << "Invalid choice!\n";
        }
    }
}