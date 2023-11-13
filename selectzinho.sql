SELECT pst.pstnome, bch.bchnome, rep.repnome, SUM(arq.arqtamanho) as TamanhoTotalPasta
FROM pasta pst, arquivo arq, branch bch, repositório rep
WHERE bch.repid = rep.repid AND pst.bchid = bch.bchid AND pst.pstid = arq.pertenceapstid
GROUP BY rep.repnome, bch.bchnome, pst.pstnome
ORDER BY TamanhoTotalPasta;

SELECT pst.pstnome, bch.bchnome, rep.repnome, usr.usrid, SUM(arq.arqtamanho) as TamanhoTotalPasta
FROM pasta pst, arquivo arq, branch bch, repositório rep, usuário usr
WHERE usr.usrid = rep.usrid AND bch.repid = rep.repid AND pst.bchid = bch.bchid AND pst.pstid = arq.pertenceapstid
GROUP BY usr.usrid, rep.repnome, bch.bchnome, pst.pstnome
ORDER BY TamanhoTotalPasta;