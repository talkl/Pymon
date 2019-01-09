import React from "react";
import {BUTTONS} from "../config"
import SimonBtn from "./button"
import {getGameId, ajax} from "../utils"


export default class Simon extends React.Component {
    constructor(props){
        super(props);
        this.state = {activeBtn:"none", sequenceStep:0};
        this.sounds = {};
        BUTTONS.map(b => {
            this.sounds[b] = new Audio(`/sounds/${b}.mp3`);
        });
    }

    activateBtn(color, userInitiated){
        this.setState(() => ({
            activeBtn:color
        }), () => { 
            this.sounds[color].play();
            setTimeout(() => { this.setState({activeBtn:"none"})}, 500);
        });
        if (userInitiated){
            ajax(`/games/${getGameId()}/turn`, {method: 'POST', body: JSON.stringify({"color":color})});
        }
    }

    playSequence(){
        setTimeout(() => {
            this.activateBtn(this.props.sequence[this.state.sequenceStep], false)
            this.setState((prevState, props) => ({
                sequenceStep: prevState.sequenceStep + 1
            }), () => { 
                if (this.state.sequenceStep < this.props.sequence.length){
                    this.playSequence();
                }else{
                    ajax(`/games/${getGameId()}/players`, {method: 'PUT'})
                }
            }); 
           
        }, ((this.state.sequenceStep == 0) ? 0 : 1500));
    }

 

    render() {
        return <div className="simon" >
            {BUTTONS.map(b => (
                <SimonBtn  key={b} color={b} active={this.state.activeBtn == b} disabled={this.props.disabled} clickAction={this.activateBtn.bind(this)} />
            ))}
            { this.state.sequenceStep == 0 && this.props.showPlayBtn &&
            <button className="play-btn" onClick={this.playSequence.bind(this)}>Play</button>
            }
            </div>
    }
}