# puralax-simulator
A python App that simulates puralax game and shows the best path to win

After playing puralax and left the game with some unresolved levels I decided to make an App to help me.
but my main goal was learning python lang with real practice. so you find my code very similar to java and too OOP:-D
	
# how to play
 After converting game board to my format you can execute Simulate.py with arguments to see how you can won the game.
 <br><br><img src="http://uupload.ir/files/kt82_capturezzz.png" align="center"/><br><br>
 for this example your arguments should be: 
 	<br>	`" blue:1 purple:1 purple:0 red:0 2 2"`<br>
 you can replace your color name with an unique name for less typing. in abbove exmaple "blue" can be replaced with "b" etc.
 if a cell was empty you can show that with "0" and when a cell was blocked you can show that with "#"
 last argument is height of the board and previous arg is width of the board.
 
 - sample output for this example:<br>
    `1-purple[↓]`<br>
    `0-blue[↓]`
<br>
It means purple cell at index 1 should be move down and after that blue cell at index 0 should move down to win the game.

just attention this algorithm order is depend on available moving cells and is:<br> 	`(n!)*(4^n)`<br>
depend on your input board it might take several time to calculate.
 	 
	


		
