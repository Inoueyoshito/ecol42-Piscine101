#!/bin/bash

[ $# -ne 1 ] && exit 1
grep $1 -lr . | sort