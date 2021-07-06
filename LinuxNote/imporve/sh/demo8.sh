#!/bin/bash
PS3="Please choose the menu: "
select menu in mifan huimian jiaozi babaozhou quit; do
  case $REPLY in
  1 | 4)
    echo "the price is 15"
    ;;
  2 | 3)
    echo "the price is 20"
    ;;
  5)
    break
    ;;
  *)
    echo "no the option"
    ;;
  esac
done
