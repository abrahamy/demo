Attribute VB_Name = "test_findreplacer"
Sub replaceMultipleCharactersInString()

    'This code is an Excel macro that does a find replace in a worksheet
    'Actually its not completed

    'declare object variable to hold reference to cell you work with
    Dim myCell As Range

    'declare variables to hold string you work with and replacement character
    Dim myString As String
    Dim myReplacementCharacter As String

    'declare variable to hold Variant containing array whose elements are characters to replace, and variable used to iterate through the elements of the array
    Dim myCharactersArray() As Variant
    Dim iCharacter As Variant

    'identify the cell you work with and the string within that cell
    Set myCell = ThisWorkbook.Worksheets("Sheet1").Range("A2")
    myString = myCell.Value

    'specify elements of array (characters to replace) and replacement character
    myCharactersArray = Array("(", ",", ")", "/", "&", ".", "@", "-", "_", ">", "  ")
    myReplacementCharacter = " "

    'loop through each element (iCharacter) of the array (myCharacterArray)
    For Each iCharacter In myCharactersArray

        'replace all occurrences of element (iCharacter) within current version of string you work with (myString), and assign resulting string to myString variable
        myString = Replace(Expression:=myString, Find:=iCharacter, Replace:=myReplacementCharacter)

    Next iCharacter

    'assign string represented by myString variable to Range.Value property of cell you work with
    myCell.Value = myString

End Sub
