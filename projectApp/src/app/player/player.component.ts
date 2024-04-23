/* d */

import { Component } from '@angular/core';
import {ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { WebService } from '../web.service';



@Component({
  selector: 'player',
  templateUrl: './player.component.html',
  styleUrls: ['./player.component.css']
})

export class PlayerComponent {

  public commentForm: any;

  public player: any = [];
  public playerIdParam: string = "";
  public comments: any = [];

  /* Constructors for calling the webService, AuthService, and FormBuilder */

  constructor(public webService: WebService,
              private route: ActivatedRoute,
              private formBuilder: FormBuilder) { }
  ngOnInit(){
    this.playerIdParam = this.route.snapshot.params['id'];
    this.commentForm = this.formBuilder.group({
      comment: ['', Validators.required]
    });

    this.player = this.webService.getPlayer(this.playerIdParam);
  }


  onSubmit() {
    console.log(this.commentForm.value);

    this.webService.postComment(this.playerIdParam, this.commentForm.value)
      .subscribe( (_: any) => {
      this.commentForm.reset();
      //this.comments = this.webService.getmanagersComments(this.playerIdParam);
      this.player = this.webService.getPlayer(this.playerIdParam);
    });

  }

  /* Validation to confirm that form data has been entered and done so correctly */

  isInvalid(control: any) {
    return this.commentForm.controls[control].invalid && this.commentForm.controls[control].touched;
  }

  isUntouched() {
    return this.commentForm.controls.comment.pristine
  }

  isIncomplete(){
    return this.isInvalid('comment') ||
    this.isUntouched();
  }

}

