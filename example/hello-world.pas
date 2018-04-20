program Hello-World;

uses crd;

var i:integer;

begin
    WriteLn('Hello world');
    if (true) then begin
        WriteLn('!');
    end;

    for i:=0 to 10 do begin
        WriteLn(i);
    end;
end.
