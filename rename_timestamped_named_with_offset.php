<?php

$good_extensions = ['JPG'];

$dir = new DirectoryIterator(dirname(__FILE__));
foreach ($dir as $fileinfo) {
  if (!$fileinfo->isDot() && in_array($fileinfo->getExtension(), $good_extensions)) {
      $old_timestamp = $fileinfo->getBasename('.JPG');
      $new_timestamp = intval($old_timestamp) + 43200;
      rename($old_timestamp . '.JPG', $new_timestamp . '.JPG');
    }
}
