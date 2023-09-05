import React, { useState } from "react";
import "./App.css";

import Additem from "./components/additem";
import Todolist from "./components/todolist";

const App = () => {

    const [listitems, setlistitems] = useState(
        [
            { itemid: Math.trunc(Math.random() * 100 + 1), itemname: "watch tv" },
            { itemid: Math.trunc(Math.random() * 100 + 1), itemname: "buy gold" },
            { itemid: Math.trunc(Math.random() * 100 + 1), itemname: "drive car" }
        ])
    const additemhandler = (newitem) => {
        setlistitems((previouslist) => {
            return previouslist.concat(newitem)
        })
    }

    const name = "MERN"

    return (
        <div className="container">
            <h1> {name}'s Todo list</h1>
            <Todolist list={listitems} />
            <Additem onadditem={additemhandler} />
        </div>
    );
};
export default App;
