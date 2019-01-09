import React from "react";

export default class SequenceLight extends React.Component {
    render() {
        return <div className="sequence-light">
            {this.props.show && <div className="inner-light" style={{backgroundColor:this.props.color}}></div>}
        </div>
    }
}