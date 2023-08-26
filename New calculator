#!/data/data/com.termux/files/usr/bin/bash

# Color codes
GREEN="\e[32m"
YELLOW="\e[33m"
CYAN="\e[36m"
RESET="\e[0m"

# Display developer information
echo -e "${CYAN}========================================${RESET}"
echo -e "${CYAN}  Developer: Crazy Hackers${RESET}"
echo -e "${CYAN}  Contact: +918950027349 (WhatsApp)${RESET}"
echo -e "${CYAN}========================================${RESET}"

# Function to perform addition
add() {
    echo -e "${GREEN}Enter the first number:${RESET}"
    read num1
    echo -e "${GREEN}Enter the second number:${RESET}"
    read num2
    result=$((num1 + num2))
    echo -e "${YELLOW}Result: $result${RESET}"
}

# Function to perform subtraction
subtract() {
    echo -e "${GREEN}Enter the first number:${RESET}"
    read num1
    echo -e "${GREEN}Enter the second number:${RESET}"
    read num2
    result=$((num1 - num2))
    echo -e "${YELLOW}Result: $result${RESET}"
}

# Function to perform multiplication
multiply() {
    echo -e "${GREEN}Enter the first number:${RESET}"
    read num1
    echo -e "${GREEN}Enter the second number:${RESET}"
    read num2
    result=$((num1 * num2))
    echo -e "${YELLOW}Result: $result${RESET}"
}

# Function to perform division
divide() {
    echo -e "${GREEN}Enter the dividend:${RESET}"
    read num1
    echo -e "${GREEN}Enter the divisor:${RESET}"
    read num2
    result=$(awk "BEGIN {printf \"%.2f\", $num1 / $num2}")
    echo -e "${YELLOW}Result: $result${RESET}"
}

# Main menu
while true; do
    echo -e "${CYAN}========================================${RESET}"
    echo -e "${CYAN}  Fancy Calculator${RESET}"
    echo -e "${CYAN}========================================${RESET}"
    echo -e "${GREEN}1. Add${RESET}"
    echo -e "${GREEN}2. Subtract${RESET}"
    echo -e "${GREEN}3. Multiply${RESET}"
    echo -e "${GREEN}4. Divide${RESET}"
    echo -e "${GREEN}5. Exit${RESET}"
    echo -e "${CYAN}========================================${RESET}"

    read choice

    case $choice in
        1) add ;;
        2) subtract ;;
        3) multiply ;;
        4) divide ;;
        5) exit ;;
        *) echo -e "${YELLOW}Invalid choice${RESET}" ;;
    esac
done
