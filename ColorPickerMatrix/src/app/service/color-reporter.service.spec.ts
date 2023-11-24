import { TestBed } from '@angular/core/testing';

import { ColorReporterService } from './color-reporter.service';

describe('ColorReporterService', () => {
  let service: ColorReporterService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ColorReporterService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
