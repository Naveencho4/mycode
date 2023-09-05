import React from "react";
import "./additem.css";

const Additem = (props) => {
    let entry = '';

    const submithandler = (event) => {
        event.preventDefault();

        const newitem = {
            itemid: Math.trunc(Math.random() * 100 + 1),
            itemname: entry,

        }
        props.onadditem(newitem);
    };

    const entryhandler = (event) => {

        entry = event.target.value;
    }


    return (
        <form className="form" onSubmit={submithandler}>
            <input type="text" onChange={entryhandler} />
            <button type="submit"> add</button>
        </form>
    )
};

export default Additem