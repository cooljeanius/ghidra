## ###
#  IP: GHIDRA
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
##
# Examples of basic Ghidra scripting in Python
# @category: Examples.Python
# @runtime Jython

# Get info about the current program
import time
from ghidra.util.data.DataTypeParser import AllowedDataTypes
from ghidra.app.util.datatype import DataTypeSelectionDialog
print
print "Program Info:"
program_name = currentProgram.getName()
creation_date = currentProgram.getCreationDate()
language_id = currentProgram.getLanguageID()
compiler_spec_id = currentProgram.getCompilerSpec().getCompilerSpecID()
print "%s: %s_%s (%s)\n" % (program_name, language_id, compiler_spec_id, creation_date)

# Get info about the current program's memory layout
print "Memory layout:"
print "Imagebase: " + hex(currentProgram.getImageBase().getOffset())
for block in getMemoryBlocks():
    start = block.getStart().getOffset()
    end = block.getEnd().getOffset()
    print "%s [start: 0x%x, end: 0x%x]" % (block.getName(), start, end)
print

# Get the current program's function names
function = getFirstFunction()
while function is not None:
    print function.getName()
    function = getFunctionAfter(function)
print

# Get the address of the current program's current location
print "Current location: " + hex(currentLocation.getAddress().getOffset())

# Get some user input
val = askString("Hello", "Please enter a value")
print val

# Output to a popup window
popup(val)

# Add a comment to the current program
minAddress = currentProgram.getMinAddress()
listing = currentProgram.getListing()
codeUnit = listing.getCodeUnitAt(minAddress)
codeUnit.setComment(codeUnit.PLATE_COMMENT, "This is an added comment!")

# Get a data type from the user
tool = state.getTool()
dtm = currentProgram.getDataTypeManager()
selectionDialog = DataTypeSelectionDialog(
    tool, dtm, -1, AllowedDataTypes.FIXED_LENGTH)
tool.showDialog(selectionDialog)
dataType = selectionDialog.getUserChosenDataType()
if dataType != None:
    print "Chosen data type: " + str(dataType)

# Report progress to the GUI.  Do this in all script loops!
monitor.initialize(10)
for i in range(10):
    monitor.checkCanceled()  # check to see if the user clicked cancel
    time.sleep(1)  # pause a bit so we can see progress
    monitor.incrementProgress(1)  # update the progress
    monitor.setMessage("Working on " + str(i))  # update the status message
