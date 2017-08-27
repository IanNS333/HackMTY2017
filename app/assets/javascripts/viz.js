var game = new Phaser.Game(800, 600, Phaser.AUTO, 'phaser-example', { preload: preload, create: create, update: update, render: render });

function preload(){
  game.load.image('user1','../../assets/blueArrow.png');//user1
  game.load.image('user2','../../assets/redArrow.png');//user2
  game.load.image('flag','../../assets/checkered.png');//
  game.load.image('obstacle','../../assets/block.png');//
}

//JSON shit
var j='{ "board": {       "obstacles": [           [3,3],           [20,20]       ],       "start" : [50,50],       "end" : [0,0],   },   "Player1" : [       [           [0,0,0,1,0,2,1,2,2],           [0,1,2,1,2,0,1,2,3]       ],       [           [0,0,0,1,0,2,1,2,2],           [0,1,2,1,2,0,1,2,3]       ]   ],   "Player2" :[                    #player       [                                #generation           [0,0,0,1,0,2,1,2,2],            #genome           [0,1,2,1,2,0,1,2,3]       ],       [           [0,0,0,1,0,2,1,2,2],           [0,1,2,1,2,0,1,2,3]       ]   ] }'
var json=JSON.parse(j);

var spriteA= new Array();//Sprites
var genomeA= new Array();//Gerardo shit
var counterA= new Array();//Sum count genome
var spriteB= new Array();
var genomeB= new Array();
var counterB= new Array();
var obstacles= new Array();//Sprites
var obstacleCoord= new Array();//Gerardo shit

var flag;
var start;
//TEMP VALUES
var playerNo=10;
var obstaclesNo=50;
var currentgen;// IMPORTANT
var currentStringpos=1;

function restartThings(){

  //SPRITES
  flag=game.add.sprite(flag[0],flag[1],'flag'); //change coord
  game.physics.enable(flag, Phaser.Physics.ARCADE);

  for(var i=0;i<genomeA[0].length;i++){  //counter for sums
    counterA[i]=0;
    counterB[i]=0;
  }

  //Add USERS to arrays and alive
  for(var i=0;i<genomeA[0].length;i++){
    spriteA[i]=game.add.sprite(playerStartX,playerStartY,'user1');
    if(genomeA[currentgen][i][0]==7){
      spriteA[i].angle(-45);
    }else if(genomeA[currentgen][i][0]==1){
      spriteA[i].angle(45);
    }else if(genomeA[currentgen][i][0]==2){
      spriteA[i].angle(90);
    }else if(genomeA[currentgen][i][0]==3){
      spriteA[i].angle(135);
    }else if(genomeA[currentgen][i][0]==4){
      spriteA[i].angle(180);
    }else if(genomeA[currentgen][i][0]==5){
      spriteA[i].angle(-135);
    }else if(genomeA[currentgen][i][0]==6){
      spriteA[i].angle(-90);
    }
    spriteA[i].alive=true;  //Just in case for now
    spriteB[i]=game.add.sprite(playerStartX,playerStartY,'user2');
    if(genomeB[currentgen][i][0]==7){
      spriteB[i].angle(-45);
    }else if(genomeB[currentgen][i][0]==1){
      spriteB[i].angle(45);
    }else if(genomeB[currentgen][i][0]==2){
      spriteB[i].angle(90);
    }else if(genomeB[currentgen][i][0]==3){
      spriteB[i].angle(135);
    }else if(genomeB[currentgen][i][0]==4){
      spriteB[i].angle(180);
    }else if(genomeB[currentgen][i][0]==5){
      spriteB[i].angle(-135);
    }else if(genomeB[currentgen][i][0]==6){
      spriteB[i].angle(-90);
    }
    spriteB[i].alive=true;  //Just in case for now

    counterA[i]=genomeA[currentgen][i][0];
    counterB[i]=genomeB[currentgen][i][0];
  }
  game.physics.enable(spriteA, Phaser.Physics.ARCADE);
  game.physics.enable(spriteB, Phaser.Physics.ARCADE);
}

function create(){
  game.physics.startSystem(Phaser.Physics.ARCADE);  //NECESSARY... I THINK...
  currentgen=0;

  //Get shit from JSON
  genomeA=json.Player1;  //[ gen1[g1[],[],[],[],[]], gen2[g2[],[],[],[]] ]
  genomeB=json.Player2;
  obstacleCoord=json.board; //[ [x,y], [x1,y1] ]
  flag=json.flag; //TELL GERARDO [x,y]
  //start=json.start; start place

  restartThings();

  //Add OBSTACLES to arrays and alive
  for(var i=0;i<obstacleCoord.length;i++){
    obstacles[i]=game.add.sprite(obstacleCoord[i][0],obstacleCoord[i][1],'obstacle');
  }
  game.physics.enable(obstacles, Phaser.Physics.ARCADE);

  //STOP

  // PAUSE/PLAY
  // pauseClick = this.input.keyboard.addKey(Phaser.Keyboard.SPACEBAR);
  // spaceKey.onDown.add(togglePause, this);
  // IF PRESSED PAUSE, IT PAUSES LIKE THIS
}

function togglePause(){
  game.physics.arcade.isPaused = (game.physics.arcade.isPaused) ? false : true;
}

function toggleStop(){

}

function update(){ //PHYSICS SHIT calculate
  on=true;
  if(currentStringpos>genomeA[0][0].length){
    currentStringpos=0;
    currentgen++;
    restartThings();
  }
  for(var i=0;i<genomeA[0][0].length;i++){
    if(genomeA[currentgen][i][currentStringpos]==0){
      counterA[i]--;
      if(counterA[i]<0){
        counterA[i]=7;
      }
      spriteA[i].angle(-45);
    }else if(genomeA[currentgen][i][currentStringpos]==2){
      counterA[i]++;
      if(counterA[i]>7){
        counterA[i]=0;
      }
      spriteA[i].angle(45);
    }
    if(counterA[i]==0){
      moveToXY(spriteA[i],spriteA[i].x+20,spriteA[i].y,10);
    }else if(counterA[i]==1){
      moveToXY(spriteA[i],spriteA[i].x+10,spriteA[i].y-10,10);
      moveToXY(spriteA[i],spriteA[i].x+10,spriteA[i].y-10,10);
    }else if(counterA[i]==2){
      moveToXY(spriteA[i],spriteA[i].x,spriteA[i].y-20,10);
    }else if(counterA[i]==3){
      moveToXY(spriteA[i],spriteA[i].x-10,spriteA[i].y-10,10);
      moveToXY(spriteA[i],spriteA[i].x-10,spriteA[i].y-10,10);
    }else if(counterA[i]==4){
      moveToXY(spriteA[i],spriteA[i].x-20,spriteA[i].y,10);
    }else if(counterA[i]==5){
      moveToXY(spriteA[i],spriteA[i].x-10,spriteA[i].y+10,10);
      moveToXY(spriteA[i],spriteA[i].x-10,spriteA[i].y+10,10);
    }else if(counterA[i]==6){
      moveToXY(spriteA[i],spriteA[i].x,spriteA[i].y+20,10);
    }else if(counterA[i]==7){
      moveToXY(spriteA[i],spriteA[i].x+10,spriteA[i].y+10,10);
      moveToXY(spriteA[i],spriteA[i].x+10,spriteA[i].y+10,10);
    }

    if(genomeB[currentgen][i][currentStringpos]==0){
      counterB[i]--;
      if(counterB[i]<0){
        counterB[i]=7;
      }
      spriteB[i].angle(-45);
    }else if(genomeB[currentgen][i][currentStringpos]==2){
      counterB[i]++;
      if(counterB[i]>7){
        counterB[i]=0;
      }
      spriteB[i].angle(45);
    }
    if(counterB[i]==0){
      moveToXY(spriteB[i],spriteB[i].x+20,spriteB[i].y,10);
    }else if(counterB[i]==1){
      moveToXY(spriteB[i],spriteB[i].x+10,spriteB[i].y-10,10);
      moveToXY(spriteB[i],spriteB[i].x+10,spriteB[i].y-10,10);
    }else if(counterB[i]==2){
      moveToXY(spriteB[i],spriteB[i].x,spriteB[i].y-20,10);
    }else if(counterB[i]==3){
      moveToXY(spriteB[i],spriteB[i].x-10,spriteB[i].y-10,10);
      moveToXY(spriteB[i],spriteB[i].x-10,spriteB[i].y-10,10);
    }else if(counterB[i]==4){
      moveToXY(spriteB[i],spriteB[i].x-20,spriteB[i].y,10);
    }else if(counterB[i]==5){
      moveToXY(spriteB[i],spriteB[i].x-10,spriteB[i].y+10,10);
      moveToXY(spriteB[i],spriteB[i].x-10,spriteB[i].y+10,10);
    }else if(counterB[i]==6){
      moveToXY(spriteB[i],spriteB[i].x,spriteB[i].y+20,10);
    }else if(counterB[i]==7){
      moveToXY(spriteB[i],spriteB[i].x+10,spriteB[i].y+10,10);
      moveToXY(spriteB[i],spriteB[i].x+10,spriteB[i].y+10,10);
    }
  }
  currentStringpos++;
}

function render(){  //JUST DRAW
  if(on){
    game.debug.text('Generation '+currentgen+1, 32, 32);
  }
}
