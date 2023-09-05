import React from "react";
import "./todolist.css";

import "./additem.css"

const Todolist = (props) => {
    console.log(props);
    return (<ul className="todolist">
        {props.list.map((listitem) => {
            return <li key={listitem.itemid}>{listitem.itemname}</li>
        }

        )}



        {/* <li>{props.list[0].itemname}</li>
        <li>{props.list[1].itemname}</li>
        <li>{props.list[2].itemname}</li> */}



    </ul>
    );
};


export default Todolist;