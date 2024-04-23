import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss',
})
export class LoginComponent implements OnInit {


  public userName: any;
  public password: any;

  ngOnInit(): void {
    this.userName = "";
    this.password = "";
  }

  Login(){
    console.log("Login");
    console.log("Username:", this.userName);
    console.log("Password:", this.password);
  }
}
