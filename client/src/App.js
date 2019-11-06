import React, {Component} from 'react';
import './App.css';
import axios from 'axios';

const getHome = async () => {
  const result = await axios.get("http://localhost:5000/")
  return result.data
}

const getName = async (first_name, last_name) => {
  const result = await axios.post("http://localhost:5000/name", {first_name, last_name})
  return result.data
}

const getAllName = async () => {
  const result = await axios.get("http://localhost:5000/all")
  return result.data.names
}

class App extends Component {
  state = {
    firstName: "",
    lastName: "",
    data: "",
    names:[]
  };

  componentDidMount(){
    getHome()
    .then(res => this.setState({data: res}))

  }

  handleInputChange = event => {
    const { name, value } = event.target;
    this.setState({
      [name]: value
    });
  };

  handleFormSubmit = event => {
    event.preventDefault();
    getName(this.state.firstName, this.state.lastName)
    .then(res => this.setState({data: res}))
  };

  handleGetAll = event => {
    event.preventDefault();
    getAllName()
    .then(res => this.setState({names: res}))
  };

  render() { 
    return ( 
      <>
        {/* <div>
          {this.state.data}
        </div> */}
        <form className="form">
          <input
            value={this.state.firstName}
            name="firstName"
            onChange={this.handleInputChange}
            type="text"
            placeholder="First Name"
          />
          <input
            value={this.state.lastName}
            name="lastName"
            onChange={this.handleInputChange}
            type="text"
            placeholder="Last Name"
          />
          <button onClick={this.handleFormSubmit}>Submit</button>
          <button onClick={this.handleGetAll}>Get All</button>
        </form>
        <div>
          {this.state.names.map(i => <div>{`Xin chào ${i.first_name} ${i.last_name}`}</div>)}
        </div>
      </>
     );
  }
}
 
export default App;
