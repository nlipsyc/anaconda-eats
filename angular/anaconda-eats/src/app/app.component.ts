import { Component } from '@angular/core';
import { tap } from 'rxjs';
import { AnacondaEatsService } from './api/anaconda-eats.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'anaconda-eat';

  constructor(private anacondaEats: AnacondaEatsService) {

  }
}
