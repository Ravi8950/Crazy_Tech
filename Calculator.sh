#!/data/data/com.termux/files/usr/bin/bash

# Display developer information
echo "========================================"
echo "  Developer: Crazy Hackers"
echo "  Contact: +918950027349 (WhatsApp)"
echo "========================================"

# Function to perform addition
add() {
    echo "Enter the first number: "
    read num1
    echo "Enter the second number: "
    read num2
    result=$((num1 + num2))
    echo "Result: $result"
}

# Function to perform subtraction
subtract() {
    echo "Enter the first number: "
    read num1
    echo "Enter the second number: "
    read num2
    result=$((num1 - num2))
    echo "Result: $result"
}

# Function to perform multiplication
multiply() {
    echo "Enter the first number: "
    read num1
    echo "Enter the second number: "
    read num2
    result=$((num1 * num2))
    echo "Result: $result"
}

# Function to perform division
divide() {
    echo "Enter the dividend: "
    read num1
    echo "Enter the divisor: "
    read num2
    result=$(awk "BEGIN {printf \"%.2f\", $num1 / $num2}")
    echo "Result: $result"
}

# Main menu
echo "========================================"
echo "  Fancy Calculator"
echo "========================================"
echo "1. Add"
echo "2. Subtract"
echo "3. Multiply"
echo "4. Divide"
echo "5. Exit"
echo "========================================"

read choice

case $choice in
    1) add ;;
    2) subtract ;;
    3) multiply ;;
    4) divide ;;
    5) exit ;;
    *) echo "Invalid choice" ;;
esac
