var game = new Phaser.Game()

function preload(){
  game.load.image('user1','where_the_fuck.png');//user1
  game.load.image('user2','where_the_fuck.png');//user2
  game.load.image('flag','where_the_fuck.png');//
  game.load.image();//
}

var playerA= new Array();//Player Blue
var playerB= new Array();//PLayer Red
var obstacles= new Array();
var flag;

//TEMP VALUES
var playerNo=10;
var playerStartX=120;
var playerStartY=120;
var flagX=150;
var flagY=150;
var obstaclesNo=50;

function create(){

  game.physics.startSystem(Phaser.Physics.ARCADE);  //NECESSARY... I THINK...

  //JSON Shit
  var j='where_the_fuck'
  var json=JSON.parse(j);

  //SPRITES
  flag=game.add.sprite(flagX,flagY,'flag');
  //Add OBSTACLES to arrays and alive
  for(var i=0;i<obstaclesNo;i++){
    // obstacles[i]=game.add.sprite();
  }
  game.physics.enable(obstacles, Phaser.Physics.ARCADE);

  //Add USERS to arrays and alive
  for(var i=0;i<playerNo;i++){
    playerA[i]=game.add.sprite(playerStartX,playerStartY,'user1');
    playerA[i].alive=true;  //Just in case for now
    playerB[i]=game.add.sprite(playerStartX,playerStartY,'user2');
    playerB[i].alive=true;  //Just in case for now
  }
  game.physics.enable(playerA, Phaser.Physics.ARCADE);
  game.physics.enable(playerB, Phaser.Physics.ARCADE);


  //STOP


  //PAUSE/PLAY
  // pauseClick = this.input.keyboard.addKey(Phaser.Keyboard.SPACEBAR);
  // spaceKey.onDown.add(togglePause, this);
  //IF PRESSED PAUSE, IT PAUSES LIKE THIS
}

function togglePause(){
  game.physics.arcade.isPaused = (game.physics.arcade.isPaused) ? false : true;
}

function toggleStop(){

}

function update(){ //PHYSICS SHIT calculate
  for()
}

function render(){  //JUST DRAW

}
