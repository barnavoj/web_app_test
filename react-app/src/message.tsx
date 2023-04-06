
function Message() {
    const name = "";
    if (name)
        return <h1>Hello {name}</h1>;
    return <h1>Hello no name specified</h1>;   
}


export default Message;