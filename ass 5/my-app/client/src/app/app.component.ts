import { Component } from '@angular/core';
import { ApiService } from './api.service';
import pkg from '../../package.json';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontEnd';
    version: any;
    message: any;
    constructor(private apiService: ApiService) { };
    ngOnInit() {
        this.apiService.getMessage().subscribe(data => {
            this.message = data;
        });
        this.version = pkg.version;
    }
}
