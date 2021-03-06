import { NgModule }      from '@angular/core';
import { CommonModule }  from '@angular/common';
import { FormsModule as AngularFormsModule } from '@angular/forms';
import { NgaModule } from '../../theme/nga.module';

import { routing }       from './forms.routing';

import { CeiboShare } from 'ng2-social-share';

import { RatingModule } from 'ng2-bootstrap';
import { Forms } from './forms.component';
import { Inputs } from './components/inputs';
import { Layouts } from './components/layouts';
import { ReactiveFormsModule } from '@angular/forms';
import { StandardInputs } from './components/inputs/components/standardInputs';
import { ValidationInputs } from './components/inputs/components/validationInputs';
import { GroupInputs } from './components/inputs/components/groupInputs';
import { CheckboxInputs } from './components/inputs/components/checkboxInputs';
import { Rating } from './components/inputs/components/ratinginputs';
import { SelectInputs } from './components/inputs/components/selectInputs';
import {GeolocationService} from './components/layouts/GeolocationService';
import { InlineForm } from './components/layouts/components/inlineForm';
import { BlockForm } from './components/layouts/components/blockForm';
import { HorizontalForm } from './components/layouts/components/horizontalForm';
import { BasicForm } from './components/layouts/components/basicForm';
import { WithoutLabelsForm } from './components/layouts/components/withoutLabelsForm';
@NgModule({
  imports: [
    CommonModule,
    AngularFormsModule,
    NgaModule,
    RatingModule.forRoot(),
    routing,
    ReactiveFormsModule
  ],
  declarations: [
    Layouts,
    Inputs,
    Forms,
    StandardInputs,
    ValidationInputs,
    GroupInputs,
    CheckboxInputs,
    Rating,
    SelectInputs,
    InlineForm,
    BlockForm,
    HorizontalForm,
    BasicForm,
    WithoutLabelsForm,
    CeiboShare
  ],
  providers: [
    GeolocationService
  ]
})
export class FormsModule {
}
