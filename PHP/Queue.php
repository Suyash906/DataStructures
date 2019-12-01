<?php

function poll($queue){
  if(0 == count($queue))
    return -1;
  $top = $queue[0];
  array_splice($queue, 0, 1);
  return array("queue"=>$queue, "data"=>$top);
}

function add($queue, $data){
  $queue[] = $data;
  return $queue;
}

function peek($queue){
  $len = count($queue);
  if(0 == $len)
    return -1;
  return $queue[0];
}

function display($queue){
  foreach ($queue as $value) {
    echo $value;
    echo "\n";
  }
  echo "\n";
  echo "\n";
}


function test(){
  $queue = [];
  $queue = add($queue, 1);
  display($queue);
  $queue = add($queue, 2);
  display($queue);
  $queue = add($queue, 3);
  display($queue);
  $queue = add($queue, 4);
  display($queue);


  $popData = poll($queue);
  print_r($popData);
  $queue = $popData["queue"];
  $poppedValue  = $popData["data"];

  display($queue);

  $popData = poll($queue);
  $queue = $popData["queue"];
  $poppedValue  = $popData["data"];

  display($queue);
}

test();
