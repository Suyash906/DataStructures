<?php

function pop($stack){
  if(0 == count($stack))
    return -1;
  $top = $stack[0];
  array_splice($stack, 0, 1);
  return array("stack"=>$stack, "data"=>$top);
}

function push($stack, $data){
  $res = [];
  $res[0] = $data;
  $i=0;
  foreach ($stack as $value) {
    $res[$i+1] = $stack[$i];
    $i++;
  }
  return $res;
}

function peek($stack){
  if(0 == count($stack))
    return -1;
  return $stack[0];
}

function display($stack){
  foreach ($stack as $value) {
    echo $value;
    echo "\n";
  }
  echo "\n";
  echo "\n";
}


function test(){
  $stack = [];
  $stack = push($stack, 1);
  display($stack);
  $stack = push($stack, 2);
  display($stack);
  $stack = push($stack, 3);
  display($stack);
  $stack = push($stack, 4);
  display($stack);

  $popData = pop($stack);
  print_r($popData);
  $stack = $popData["stack"];
  $poppedValue  = $popData["data"];

  display($stack);

  $popData = pop($stack);
  $stack = $popData["stack"];
  $poppedValue  = $popData["data"];

  display($stack);
}

test();

