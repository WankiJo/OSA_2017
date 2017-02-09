/**
 * Created by rim on 2017-02-09.
 */
var express = require('express');
var app = express();
var http = repuire('http').Server(app);
var io = require('socket.io')(http);

app.get("/",function(req,res){
    res.sendfile("ChatClient.html");
});

var count=1;
io.on('connection',function(socket){
    console.log('user connected: ',socket.id);
    var name="user"+count++;
    io.to(socket.id).emit('change name',name);//이벤트 쏠때//io(.to('받는 사람 소켓아이디'))(한명항테쓸때).emit('이벤트이름',객체)//이벤트 보낸사람도 받는다

    socket.on('disconnet',function(){//이벤트 받을 때//socket.on('이벤트 이름',객체)
        console.log('user disconnected: ',soxket.id);
    });

    socket.on('send message',function(name,text){
        var msg = name + ' : '+text;
        console.log(msg);
        io.emit('receive message',msg);
    });
});

http.listen('3000',function(){
    console.log("server.on!");
});