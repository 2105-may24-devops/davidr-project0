#!/usr/bin/env bash

main () {

    if [[ $1 == "attack" || $1 == "all" ]]; then
        cp ./scripts/attack_template.txt ./scripts/attack_test.txt
        success_counter=0

        for i in {1..5}; do
            echo "Running Attack test #$i"
        
            player_attack=$(($RANDOM % 150))
            enemy_attack=$(($RANDOM % 150))
            both_hp=100

            sed -i "s/{player_attack}/$player_attack/" ./scripts/attack_test.txt
            sed -i "s/{player_hp}/$(( both_hp - enemy_attack >= 0 ? both_hp - enemy_attack : 0 ))/" ./scripts/attack_test.txt
            sed -i "s/{enemy_attack}/$enemy_attack/" ./scripts/attack_test.txt
            sed -i "s/{enemy_hp}/$(( both_hp - player_attack >= 0 ? both_hp - player_attack : 0 ))/" ./scripts/attack_test.txt

            py -m main attack $player_attack $enemy_attack > ./scripts/output.txt

            file1="./scripts/output.txt"
            file2="./scripts/attack_test.txt"
            

            if diff --strip-trailing-cr "$file1" "$file2"; then
                echo "Attack test #$i passed"
                (( success_counter = success_counter + 1 ))
            else
                echo "Attack test #$i failed"
            fi

            cp ./scripts/attack_template.txt ./scripts/attack_test.txt
        done
        echo "$success_counter/5 Attack tests passed"

        if [[ $success_counter < 5 ]]; then
            echo "Not all Attack tests passsed" 1>&2
            exit 1
        fi
    fi

    if [[ $1 == "guard" || $1 == "all" ]]; then
        cp ./scripts/guard_template.txt ./scripts/guard_test.txt
        success_counter=0

        for i in {1..5}; do
            echo "Running Guard test #$i"
        
            player_attack=$(($RANDOM % 150))
            enemy_attack=$(($RANDOM % 150))
            player_defense=$(($RANDOM % 150))
            enemy_defense=$(($RANDOM % 150))
            both_hp=100
            player_damage=$(( player_attack - enemy_defense >= 0 ? player_attack - enemy_defense : 0 ))
            enemy_damage=$(( enemy_attack - player_defense >= 0 ? enemy_attack - player_defense : 0 ))

            sed -i "s/{player_damage}/$player_damage/" ./scripts/guard_test.txt
            sed -i "s/{player_hp}/$(( both_hp - enemy_damage >= 0 ? both_hp - enemy_damage: 0 ))/" ./scripts/guard_test.txt
            sed -i "s/{enemy_damage}/$enemy_damage/" ./scripts/guard_test.txt
            sed -i "s/{enemy_hp}/$(( both_hp - player_damage >= 0 ? both_hp - player_damage : 0 ))/" ./scripts/guard_test.txt

            py -m main guard $player_attack $enemy_attack $player_defense $enemy_defense> ./scripts/output.txt

            file1="./scripts/output.txt"
            file2="./scripts/guard_test.txt"
            

            if diff --strip-trailing-cr "$file1" "$file2"; then
                echo "Guard test #$i passed"
                (( success_counter = success_counter + 1 ))
            else
                echo "Guard test #$i failed"
            fi

            cp ./scripts/guard_template.txt ./scripts/guard_test.txt
        done
        echo "$success_counter/5 Guard tests passed"

        if [[ $success_counter < 5 ]]; then
            echo "Not all Guard tests passsed" 1>&2
            exit 1
        fi
    fi
    
    if [[ $1 == "save" || $1 == "all" ]]; then
        success_counter=0

        for i in {1..3}; do
            echo "Running Save test #$i"
            names_list=('Bob' 'Jack' 'Potato')
            player_name=${names_list[$(($RANDOM % 3))]}
            player_level=$((1 + $RANDOM % 150))
            player_health=40

            py -m main save player $player_name $player_level $player_health
            if [[ $(grep -c -e '"name": '"\"${player_name}\"" -e '"level": '"$player_level" -e '"health": '"$player_health" ./saves/savePLAYERTEST.json) -eq 3 ]]; then
                echo "Save test #$i passed"
                (( success_counter = success_counter + 1 ))
            else 
                echo "Save test #$i failed"
            fi
        done
        echo "$success_counter/3 Save tests passed"

        if [[ $success_counter < 3 ]]; then
            echo "Not all Save tests passsed" 1>&2
            exit 1
        fi
    fi

    echo "All tests passed"
}

main "$@"