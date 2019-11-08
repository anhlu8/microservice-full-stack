import React, {Component} from 'react';
import Button from '@material-ui/core/Button';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import axios from 'axios';

const getHome = async () => {
  const result = await axios.get("http://localhost:8000/")
  return result.data
}

const getName = async (first_name, last_name) => {
  const result = await axios.post("http://localhost:8000/name", {first_name, last_name})
  return result.data
}

const getAllName = async () => {
  const result = await axios.get("http://localhost:8000/all")
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

  handleEdit = (unique_id) => {
    console.log("edit id", unique_id)
  };

  handleDelete = (unique_id) => {
    console.log("delete id", unique_id)
  };

  render() { 
    return ( 
      <>
        <div>
          {this.state.data}
        </div>
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
          <Button size="small" variant="contained" color="primary" onClick={this.handleFormSubmit}>Submit</Button>
          <Button size="small" variant="contained" color="secondary" onClick={this.handleGetAll}>Get All</Button>
        </form>
        <Table aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell>Name</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
          {this.state.names.map((i, index) => {
              const {first_name, last_name} = i
              return (
                <TableRow key={index}>
                  <TableCell component="th" scope="row">
                    {`Xin chào ${first_name} ${last_name} `}
                  </TableCell>
                </TableRow>
              )
            }
          )}
          </TableBody>
        </Table>
      </>
     );
  }
}
 
export default App;
