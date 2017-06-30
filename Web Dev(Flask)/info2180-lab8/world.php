<?php
mysql_connect(
"0.0.0.0",
"drellimal2"
);
mysql_select_db("world");

$ALL = $_REQUEST['all'];
$LOOKUP = $_REQUEST['lookup'];

# execute a SQL query on the database
if($LOOKUP == "all"){
  $ALL = "true";
}


$results = mysql_query("SELECT * FROM countries WHERE name LIKE '%$LOOKUP%';");

if($ALL == "true"){
  $results = mysql_query("SELECT * FROM countries;");
  
# loop through each country
}
if($ALL == "false" && $LOOKUP == "" ){
  $results = "";
}

print $results;
# loop through each country

while ($row = mysql_fetch_array($results)) {
  ?>
  <li> <?php echo $row["name"]; ?>, ruled by <?php echo $row["head_of_state"]; ?> </li>
  <?php
}
?>

<?php

function sqlToXml($queryResult, $rootElementName, $childElementName)
{ 
    $xmlData = "<?xml version=\"1.0\" encoding=\"utf-8\" ?>\n"; 
    $xmlData .= "<countrydata>\n\t";
 
    while($record = mysql_fetch_object($queryResult))
    { 
        /* Create the first child element */
        $xmlData .= "<country>\n\t\t";
 
 
            $fieldName = "name"; 
 
            /* The child will take the name of the table column */
            $xmlData .= "<" . $fieldName . ">";
 
            /* We set empty columns with NULL, or you could set 
                it to '0' or a blank. */
            if(!empty($record->$fieldName))
                $xmlData .= $record->$fieldName; 
            else
                $xmlData .= "null"; 
 
            $xmlData .= "</name>\n\t\t"; 
            $fieldName = "head_of_state"; 
 
            /* The child will take the name of the table column */
            $xmlData .= "<ruler>";
 
            /* We set empty columns with NULL, or you could set 
                it to '0' or a blank. */
            if(!empty($record->$fieldName))
                $xmlData .= $record->$fieldName; 
            else
                $xmlData .= "null"; 
 
            $xmlData .= "</ruler>\n\t"; 
        
        $xmlData .= "</country>\n"; 
    } 
    $xmlData .= "</countrydata>"; 

    return $xmlData; 
}

?>






