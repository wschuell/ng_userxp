#!/bin/bash


while [[ ! -f init_done.status ]]; do
	sleep 1
done


while [[ $(cat init_done.status) -eq 1 ]]; do
	sleep 1
done


while [[ $(cat init_done.status) -eq 0 ]]; do
	sleep 1
done
