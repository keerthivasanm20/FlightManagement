from django.contrib import admin

# Register your models here.
import React, { Component } from 'react'

export default class SongComponent extends Component {
    
    
    constructor(props) {
        super(props)
    
        // this.state = {
        //      Name:'keert',
        //      host:'yes',
        //      song:{},
        // }
        // this.roomCode =this.props.match.params.room;
        // this.getcurrentsong();
        console.log("th")
    }
    
    getcurrentsong()
    {
        fetch('/currentsong'+'?code='+this.roomCode)
        .then((response) =>{
            if(!response.ok){
                   return {};
            }
            else{
               return response.json();
            }
        }).then((data)=>{
            this.setState({
                song:data
            });
            console.log(data);
        });
         
     
  
    }
   
    
    render() {
        return (
            <div id="hey" >
        hello
            
            </div>
        )
    }
}
