import { TestBed } from '@angular/core/testing';

import { AnacondaEatsService } from './anaconda-eats.service';

describe('AnacondaEatsService', () => {
  let service: AnacondaEatsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AnacondaEatsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
