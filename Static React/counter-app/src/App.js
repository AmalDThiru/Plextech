import logo from './logo.svg';
import './App.css';
import Button from "./components/Button.js";
import { useState } from 'react';





function App() {

  const[count, setCount] = useState(0);

  var increment = () => {
    setCount(count + 1)
  }
  
  var decrement = () => {
    setCount(count - 1)
  }
  
  return (
    <div className='app'>
      <h1>{count}</h1>
      <div className="button">
        <Button task={()=>decrement()} title="-"></Button>
        <Button task={()=>increment()} title="+"></Button>
      </div>
    </div>
  ) 
}






export default App;