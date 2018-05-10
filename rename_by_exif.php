<?php

$good_extensions = ['JPG', 'jpg'];

$dir = new DirectoryIterator(dirname(__FILE__));
foreach ($dir as $fileinfo) {
  if (!$fileinfo->isDot() && in_array($fileinfo->getExtension(), $good_extensions)) {
      $file_name = $fileinfo->getFilename();
      $file_name_full = dirname(__FILE__) . '/' . $file_name;
      $exif = exif_read_data($file_name_full);
      $date_taken = $exif['DateTimeOriginal'];
      $date_taken_timestamp = strtotime($date_taken);
      rename($file_name, $date_taken_timestamp . '.JPG');
    }
}
