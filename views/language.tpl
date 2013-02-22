%rebase main_template title='language ' + language + ' in ' + proj_name
<h1>Overview of the "{{language}}" language in {{pdata.name}}</h1>
% for sname, bchg, case_lst in strings:
    <h3><a href="/string/{{proj_name}}/{{language}}/{{sname}}">{{sname}}</a></h3>
    <table border="1">
    <tr><th>State<th>Case<th>Text</tr>
    % for cname, state, chg in case_lst:
        <tr><td>{{state}}<td>{{'none' if not cname else cname}}<td>{{'-' if chg is None else chg.new_text.text}}</tr>
    % end
    </table>
% end