#!/bin/bash

echo "Starting project setup"

#Step1 Creating directories
echo "Creating directory structure"
mkdir -p src data output
echo "Directories created are src, data and output"

#Step2 Creating igitignore
echo "Creating .gitignore file"
cat > .gitignore << 'EOF'
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*.pyo
*.pyd

# Virtual environments
.venv/
venv/

# Output files
output/
EOF
echo "✅ .gitignore created."


# Step 3: Create requirements.txt
echo "📦 Creating requirements.txt..."
cat > requirements.txt << 'EOF'
# Python standard libraries used for this project
pandas
numpy
EOF
echo "✅ requirements.txt created."

# Step 4: Create sample data file
echo "🧑‍🎓 Creating sample students.csv..."
cat > data/students.csv << 'EOF'
name,age,grade,subject
Alice,20,85,Math
Ashel,100,100,Math
Bob,19,92,Science
Charlie,21,78,History
Diana,20,88,Math
Evan,22,95,Science
Fiona,19,67,English
George,21,73,Math
Hannah,20,90,Science
EOF
echo "✅ data/students.csv created."



# Step 5: Create Python template files
echo "🐍 Creating Python templates..."

cat > src/data_analysis.py << 'EOF'
#!/usr/bin/env python3
"""Basic Data Analysis Script"""

def load_students(filename):
    """Load student data from CSV."""
    # TODO: Read CSV file and return data
    pass

def calculate_average_grade(students):
    """Calculate average grade."""
    # TODO: Compute and return average
    pass

def main():
    """Main analysis workflow."""
    # TODO: Implement main script logic
    pass

if __name__ == "__main__":
    main()
EOF


cat > src/data_analysis_functions.py << 'EOF'
#!/usr/bin/env python3
"""Advanced Data Analysis Functions"""

def load_data(filename):
    """Load data generically."""
    # TODO: Implement file reading logic
    pass

def analyze_data(students):
    """Perform detailed analysis."""
    # TODO: Add advanced analytics here
    pass

def main():
    """Run advanced analysis."""
    # TODO: Call other functions
    pass

if __name__ == "__main__":
    main()
EOF
echo "✅ Python templates created."

echo "🎉 Project setup complete! All files and folders are ready."