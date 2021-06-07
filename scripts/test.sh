#!/usr/bin/env bash

main () {

    if [[ $1 == "attack" ]]; then
        py -m main attack > ./scripts/output.txt

        file1="./scripts/output.txt"
        file2="./scripts/attack_test.txt"
        

        if cmp -s "$file1" "$file2"; then
            printf 'Attack test successful\n'
        else
            printf 'Attack test unsuccessful'
        fi

        diff "$file1" "$file2"
    fi

    if [[ $1 == "guard" ]]; then
        py -m main guard > ./scripts/output.txt

        file1="./scripts/output.txt"
        file2="./scripts/guard_test.txt"
        

        if cmp -s "$file1" "$file2"; then
            printf 'Guard test successful\n'
        else
            printf 'Guard test unsuccessful'
        fi

        diff "$file1" "$file2"
    fi

    # output=$() 

    # echo $output
    # if [ "$output" ==  *"Protag is attempting to attack Enemy"* ]; then
    #     echo "Correct output"
    # else 
    #     echo "Incorrect output"
    # fi
        
}

main "$@"