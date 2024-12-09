
"use strict";

let Popup = require('./Popup.js')
let IsInRemoteControl = require('./IsInRemoteControl.js')
let GetLoadedProgram = require('./GetLoadedProgram.js')
let RawRequest = require('./RawRequest.js')
let AddToLog = require('./AddToLog.js')
let Load = require('./Load.js')
let GetRobotMode = require('./GetRobotMode.js')
let GetSafetyMode = require('./GetSafetyMode.js')
let IsProgramSaved = require('./IsProgramSaved.js')
let IsProgramRunning = require('./IsProgramRunning.js')
let GetProgramState = require('./GetProgramState.js')

module.exports = {
  Popup: Popup,
  IsInRemoteControl: IsInRemoteControl,
  GetLoadedProgram: GetLoadedProgram,
  RawRequest: RawRequest,
  AddToLog: AddToLog,
  Load: Load,
  GetRobotMode: GetRobotMode,
  GetSafetyMode: GetSafetyMode,
  IsProgramSaved: IsProgramSaved,
  IsProgramRunning: IsProgramRunning,
  GetProgramState: GetProgramState,
};
