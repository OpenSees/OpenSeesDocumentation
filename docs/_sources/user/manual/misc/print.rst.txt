.. print_

print Command
*************

This command is used to print output to screen or file. There are a number of

To print all objects of the domain to a file

..function:: print <-JSON> <-file $fileName> 

To print all objects of the domain to a JSON file:

.. function:: print -JSON -file $fileName

To print node information:

.. function:: print <-file $fileName> -node <-flag $flag> <$node1 $node2 ...>

To print element information:

.. function:: print <-file $fileName> -ele <-flag $flag> <$ele1 $ele2 ...>

   $fileName    (optional) name of file to which data will be sent. overwrites existing file. default is to print to stderr)
   $flag	     integer flag to be sent to the print() method, depending on the node and element type (optional)
   $node1 $node2 ..     (optional) integer tags of nodes to be printed. default is to print all.
   $ele1 $ele2 ..	     (optional) integer tags of elements to be printed. default is to print all.

EXAMPLE:

print -ele; # print all elements

print -node 1 2 3; # print data for nodes 1,2 & 3